# Plasmid Profiler Pipeline: Heatmap display of plasmid content in WGS data

This plasmid profiler pipeline is a pipeline which parses plasmids identified through SRST2 and BLAST, scores them based on a combined measure of maximized coverage and minimized sequence divergence, and produces visualizations along with tabular results. [Input][] is provided in the form of a collection of whole genome sequence reads as well as an assembled reference genome.  The [output][] for the pipeline consists of a whole genome phylogenetic tree constructed from the detected SNVs, as well as a list of all detected SNVs and other information.

[![snv-tree][]][snv-tree]

# Operation

SNVPhyl identifies variants and generates a phylogenetic tree by mapping the input sequence reads to a reference genome followed by filtering out any invalid variant calls.  The stages are as follows:

[![snvphyl-overview][]][snvphyl-overview]

1. Preparing input files including:
    1. A set of sequence reads.
    2. A reference genome.
    3. An optional file of regions to mask on the reference genome.
2. Identification of repeat regions on the reference genome using [MUMMer][].
3. Reference mapping and variant calling using [SMALT][], [FreeBayes][] and [SAMtools/BCFtools][].
4. Merging and filtering variant calls to produce a set of high quality SNVs.
5. Generating an alignment of SNVs.
6. Building a maximum likelihood tree with [PhyML][] and generating other output files.

SNVPhyl is implemented as a [Galaxy][] workflow, with each of these stages implemented using a specific Galaxy tool.

[![plasmid-profiler-overview-galaxy][]][plasmid-profiler-overview-galaxy]

More information on the operation and installation of the pipeline can be found in the [Usage][] and [Installation][] sections.

# Contact

Comments, questions, or issues can be sent to Aaron Petkau - <aaron.petkau@phac-aspc.gc.ca>.

[Galaxy]: http://galaxyproject.org/
[Installation]: install/index.md
[Overview]: user/index.md
[SMALT]: http://www.sanger.ac.uk/resources/software/smalt/
[MUMMer]: http://mummer.sourceforge.net/
[FreeBayes]: https://github.com/ekg/freebayes
[SAMtools/BCFtools]: http://samtools.sourceforge.net/mpileup.shtml
[PhyML]: http://www.atgc-montpellier.fr/phyml/
[Usage]: user/usage.md
[snvphyl-overview]: images/snvphyl-overview.png
[plasmid-profiler-overview-galaxy]: images/plasmid-profiler-overview-galaxy.png
[snv-tree]: images/snvphyl-out.png
[output]: user/output.md
[Input]: user/input.md
