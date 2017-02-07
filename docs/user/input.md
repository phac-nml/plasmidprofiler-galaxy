# Input

This describes the main input files of the Plasmid Profiler Pipeline.  Please see the [Usage][] documentation for details on running with these input files.

# Reference Plasmid Database

This is a curated database of plasmids compiled from NCBI starting with all *Gammaproteobacteriaceae* categorized submissions (n=2797, size range: 1065-727,905 bp). It can be found in the data libraries of the Plasmid Profiler Dockerized Galaxy instance or at the [Plasmid Profiler Database][]


# Replicon Sequences and Genes of Interest

This is a multi-fasta file that can be found in the data libraries of the Plasmid Profiler Dockerized Galaxy instance or on the GitHub page: [Plasmid Finder Database][]. It is user modifiable prior to running the pipeline. The original 116 plasmid replicon sequences from [Plasmid Finder][] are supplemented by several carbepenamase genes prefixed with '(AMR)' as below. These can be replaced, added to, or removed using a text editor or Galaxy fasta tools. The '(AMR)' must remain for them to be identified by Plasmid Profiler.

```
>(AMR)GeneName_Accession
NUCLEOTIDESEQUENCE
```

# Sequence Reads

The sequence reads are the whole genome sequencing reads against which Plasmid Profiler will search for plasmids. These can be paired end or single end reads and should be in [FASTQ][] format.  Within Galaxy these should be imported with the **fastqsanger** data type and structured within a collection.

![galaxy-paired-sequence-reads][]

Please see the [Preparing Sequence Reads][] documentation for details on how to structure the data.

[Usage]: usage.md
[Plasmid Profiler Database]: https://github.com/phac-nml/plasmidprofiler-galaxy/blob/master/docker/galaxy/pp_plasmid_database.fasta.gz
[Plasmid Finder]: https://cge.cbs.dtu.dk/services/PlasmidFinder/
[Plasmid Finder Database]: https://github.com/phac-nml/plasmidprofiler-galaxy/blob/master/docker/galaxy/plasmidfinder_plusAMR.fasta
[FASTQ]: https://en.wikipedia.org/wiki/FASTQ_format
[galaxy-paired-sequence-reads]: images/galaxy-paired-sequence-reads.png
[Preparing Sequence Reads]: usage.md#preparing-sequence-reads


