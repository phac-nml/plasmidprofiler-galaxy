# Example Run

## Running the Pipeline in Galaxy

See [Running the workflow][] for how to run the pipeline in Galaxy.

## Simple analysis of the Output in R

First download two datasets from the galaxy pipeline...  

**Blast results**:  

    ##: megablast REPLICON_DATABASE_NAME vs nucleotide BLAST database from data ##  

**SRST2 results**:  

    ##: Combine on data ##, data ##, and others  

Depending on the number of samples and datasets in the history and the name of replicon database; the ## values and name will change.  

For example...  

**Blast results**:  

	88: megablast plasmidfinder_plusAMR.fasta vs nucleotide BLAST database from data 86  

**SRST2 results**:  

	82: Combine on data 75, data 70, and others

In this next step we have renamed the files to _srst2results.tsv_ and _blastresults.tsv_ for simplicity and they reside in the R Project folder.  
	
First attach the Plasmidprofiler package and then run it's main() function on the results:  

	library(Plasmidprofiler)  
	main(blast.file = "blastresults.tsv", srst2.file = "srst2results.tsv")  

This will run the following functions in order:

	read_blast() - Import the blast file, add column names  

	blast_parser() - Parse imported file  

	amr_positives() - Detect AMR positive plasmids  

	read_srst2() - Import SRST2 file  

	combine_results() - Combine SRST2 and Blast  

	zetner_score() - Add Sureness value  

	amr_presence() - Add detected AMR to report  

	subsampler() - Apply filters to report  

	order_report() - Arrange report  

	save_files() - Save JPG and CSV  

	create_plotly() - Creates plot  

	save_files() - Save HTML plot  

## Using the other functions

First attach the Plasmidprofiler package and then import the output files into your R environment:

	library(Plasmidprofiler)  
	read_blast("blastresults.tsv")  
	read_srst2("srst2results.tsv")

Next perform the initial parsing and 


## Resulting Data




[Running the workflow]: ../user/usage/#running-the-workflow