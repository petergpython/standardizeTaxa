# standardizetaxa - check a list against a source of taxa and return the accepted taxa

# How to use it
Run function standardize:  standardize(input_pandas_dataframe, threshold = 0.8)

Input_pandas_dataframe should have a column named full_taxa_input with the taxa to be standardized 

Return a dictionary with Keys 'dataframe'  and 'taxa_reconciliation_table'. The dataframe include an additional column taxa_standardized

The taxa_reconciliation_table shows:
  -input name: is the name that was fed to the https://verifier.globalnames.org API 

  -matched_name: is the name that was found to be the best match with the selected threshold (0.8).   

  -match type: is the type of match between input_name and matched_name

  -status: is the taxonomic status (according to the selected source) of the matched name 

  -output_name: is always the accepted name (according to the source used)
so even if the matched name was found to be a synonym of an accepted name, then the script fetches the accepted name and writes it in the output name, if the status says 'synonym' that refers to the matched_name, the output_name should always be an accepted name. The output_name is the one that at the end is added by the script to the dataframe in the column taxa_standardized, so taxa_standardized is always an accepted name unless it says no_matches (see file attached for the no_matches). 
