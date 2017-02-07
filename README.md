# Plasmid Profiler #
--------------------


## Legal ##
-----------

 **Plasmid Profiler -  Docker & Galaxy**

 Copyright Government of Canada 2016-2017

 Plasmid Profiler Docker and Galaxy Tools written by: Jennifer Cabral, National Microbiology Laboratory, Public Health Agency of Canada

 Plasmid Profiler R Package Written by: Adrian Zetner, National Microbiology Laboratory, Public Health Agency of Canada

 Funded by the National Micriobiology Laboratory, Public Health Agency of Canada

 Licensed under the Apache License, Version 2.0 (the "License"); you may not use
 this file except in compliance with the License. You may obtain a copy of the
 License at:

 http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software distributed
 under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
 CONDITIONS OF ANY KIND, either express or implied. See the License for the
 specific language governing permissions and limitations under the License.

## Description ##
-----------------

Heatmap display of plasmid content in WGS data. This program parses plasmids identified through SRST2 and BLAST, scores them based on a combined measure of maximized coverage and minimized sequence divergence, and produces visualizations along with tabular results. Best used on results from the workflow "P2 - Plasmid Profiler: SRST2 and BLAST"

Detailed documentation can be found at http://plasmid-profiler.readthedocs.io/. This repository contains the customized [Galaxy][] tools for this pipeline as well as the source for the documentation.

## Documentation ##
-------------------

Documentation is written using [Markdown][] and can be compiled using [mkdocs][].  To install [mkdocs][] please run:

```bash
pip install mkdocs
```

To quickly generate a site for the documentation please run:

```bash
mkdocs serve
```

This will build a site under http://localhost:8000.


[Markdown]: http://daringfireball.net/projects/markdown/syntax
[mkdocs]: http://www.mkdocs.org
[Galaxy]: https://galaxyproject.org/
