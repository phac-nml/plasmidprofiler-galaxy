## amr_positives

<h2>Identify Antimicrobial Resistance Positive Plasmids from Blast Results</h2>

<h3>Description</h3>

<p>This function loads the imported blast results, identifies which plasmids
carry AMR genes at highest identity. May have issues with multiple genes per
plasmid, currently optimized for identifying one of two genes
</p>


<h3>Usage</h3>

<pre>
amr_positives(blast.results)
</pre>


<h3>Arguments</h3>

<table summary="R argblock">
<tr valign="top"><td><code>blast.results</code></td>
<td>
<p>Blast results loaded from read_blast or from Global Env</p>
</td></tr>
</table>


<h3>Value</h3>

<p>Two column DF of plasmid names and genes present
</p>


<h3>Examples</h3>

<pre>
## Not run: 
amr_positives(blastdata)

## End(Not run)
</pre>

