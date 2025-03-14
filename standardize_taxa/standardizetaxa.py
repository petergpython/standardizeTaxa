#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import urllib3
import json
http = urllib3.PoolManager()
######
# column with taxa name to be standardized must be called "full_taxa_input"
######

def query_taxa_resolver(taxa, sources = ['196'], threshold = 0.8):
    """
    for GRIN taxonomy: source = ['6'], ['196'] for WFO 
    """
    threshold = str(threshold)
    if isinstance(taxa, str):
        taxa_format = "+".join(taxa.split())
        URL = 'https://verifier.globalnames.org/api/v1/verifications/' + taxa_format + '?data_sources=' + "|".join(sources) + '&all_matches=false&capitalize=true&species_group=false&fuzzy_uninomial=false&stats=false&main_taxon_threshold=' + threshold 
        try:
            r = http.request('GET', URL, )
            result = r.data.decode()
            result_dict = json.loads(result)
        except ValueError:
            return
    else:
        return "undetermined"
    return result_dict

def extract_best_result(list_res):
    final = []
    for i in list_res:
        match_type = i['names'][0]['matchType']
        if match_type != "NoMatch": 
           input_name  = i['names'][0]['name']
           matched_name = i['names'][0]['bestResult']['matchedName']
           output_name = i['names'][0]['bestResult']["currentName"]
           status = i['names'][0]['bestResult']['taxonomicStatus']
           final.append((input_name, matched_name, match_type, status, output_name))
        else: 
           final.append((i['names'][0]['name'], 'no_match', 'no_match', 'no_match', 'no_match'))
    return final

def run_batch_queries(df, threshold = 0.8):    
    """
    take a list of taxa and return a list of queries results
    """
    taxa_list = list(set(df["full_taxa_input"].dropna().str.strip().values))
    result_queries= []
    counter = 0
    for i in taxa_list:
        print(round(counter/len(taxa_list)*100, 2), "%", i )
        best_result = query_taxa_resolver(i, ['196'], threshold)
        result_queries.append(best_result)
        counter += 1
    return result_queries

def standardize(input_df, threshold = 0.8):
    """
    takes a dataframe return a dataframe
    column with taxa name to be standardized must be called "full_taxa_input"
    threshold argument from 0.1 to 0.99 is optional 
    """
    result_queries = run_batch_queries(input_df, threshold)
    res = extract_best_result(result_queries)
    # create a taxa dictionary to be used to map the standardised taxa to the taxa in the dataset
    taxa_standardized_df = pd.DataFrame(res)
    taxa_standardized_df.columns = ['input_name' , 'matched_name', 'match_type', 'status', 'output_name']  
    taxa_dictionary = taxa_standardized_df.set_index('input_name')[['output_name']].to_dict()['output_name']
    # add standardized taxa to the combined dataset
    input_df['taxa_standardized'] = input_df.full_taxa_input.map(taxa_dictionary)
    return input_df


