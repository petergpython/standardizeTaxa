# standardizetaxa - check a list of plant taxa against a source with a taxonomic backbone and return the accepted taxa
Python package to check a list of plant taxa against a source with one or more taxonomic backbone and return the accepted taxa from the source that gives the best result.  



# How to use it
Run function _standardize_:  standardize(input_pandas_dataframe, threshold = 0.8, sources = ['196'])

Arguments passed to the function:
-Input_pandas_dataframe is a Pandas Dataframe object and should have a column named full_taxa_input with the taxa to be standardized (i.e. 1 taxon on each row).
- The threshold value must be between 0 and 1. A taxon is considered a match when its score is equal to or higher than the threshold.
- sources is a list of strings with each one being the code of the sources (taxonomic backbones) that will be used. for ex '196' is the code for the World Flora Online. The full list of codes is avalable on https://verifier.globalnames.org 

The function _standardize_ returns a dictionary with Keys 'dataframe'  and 'taxa_reconciliation_table'. The 'dataframe' item is a Pandas dataframe including an additional column taxa_standardized, which is the accepted name of the taxon matched (i.e. the output_name in the taxa_reconciliation_table).

The taxa_reconciliation_table item is a pandas dataframe showing:
  -input name: is the name that was fed to the https://verifier.globalnames.org API 

  -matched_name: is the name that was found to be the best match with the selected threshold (0.8).   

  -match type: is the type of match between input_name and matched_name

  -status: is the taxonomic status (according to the selected source) of the matched name 
  -source: the taxonomic backbone used for this matched name

  -output_name: is always the accepted name (according to the source used)
so even if the matched name was found to be a synonym of an accepted name, then the script fetches the accepted name and writes it in the output name, if the status says 'synonym' that refers to the matched_name, the output_name should always be an accepted name. The output_name is the one that at the end is added by the script to the dataframe in the column taxa_standardized, so taxa_standardized is always an accepted name unless it says no_matches (see file attached for the no_matches). 
