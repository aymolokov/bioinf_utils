# bioinf_utils


**BioinfUtils** is a toolkit for basic operations with DNA and RNA sequences. BioinfUtils will help you with such operations on DNA and RNA as transcription, reverse transcription, finding the reversed, complementary and reversed complementary sequence. It can also filter fastq by gc-content, sequence length and read quality.

Authors:
* **Software:** *Aleksey Molokov* <br/>
[Tomsk Cancer Research Institute](https://onco.tnimc.ru/en/), Tomsk, Russia.

## Content

* [Installation](#installation)
* [Examples](#examples)
* [FAQ](#faq)
* [License](#license)
* [Contact](#contact)

## Installation

Clone repository
~~~
git clone https://github.com/aymolokov/bioinf_utils.git
~~~
Move contents to your project folder
~~~
cp -r bioinf_utils/* /path/to/your/project/
~~~
Import bioinf_utils module into your script
```python
import bioinf_utils
```


## Examples

* #### Transcription
```python
>>> bioinf_utils.run_dna_rna_tools("GATTCC", "CCAATACGTC", "comlement")
['CTAAGG', 'GGTTATGCAG']
```
* #### GC_content
```python
>>> bioinf_utils.filter_fastq_from_dict(
{
    '@SRX079804': ('TAGCTAGGACGAGGATCGT',
                   'FFFGGGFFFDGGEFDDDCC'),
    '@SRX079805': ('CAGTGCAGTGCTAGCTAGCTGACGTACGTAGCTGACTGA',
                   'GGGGGGFFEE@CEEBFDFDFFGGGEFFDDBBFFFBGFGF'),
    '@SRX079806': ('TTAGCGTAGCTAGCTAGTGGACGT',
                   'DFFDFFGGGGFFFCCCDDFFFGG!'),
    '@SRX079807': ('GATCGATCGTAGCTAGCTGACGTACTGACGATCGA',
                   'CEEEFGGGGFFDFDBBFFDDGGGFEDDDFFFF@FB'),
    '@SRX079808': ('AGGCGTACGATCGTACGTACGATCGT',
                   'GGGGFFFGGGGEFFDDCCBFGGEED@')
}
      gc_bounds=(0,60),
      length_bounds=(0, 25),
      quality_threshold=33
  )

{'@SRX079804': ('TAGCTAGGACGAGGATCGT', 'FFFGGGFFFDGvEFDDDCC'), '@SRX079806': ('TTAGCGTAGCTAGCTAGTGGACGT', 'DFFDFFGGGGFFFCCCDDFFFGG!')}
```

## FAQ

**Q**: Can I process several sequences at once?

**A**: Yes, bioinf_utils can work with a list of sequences at once

**Q**: What scale is used to assess the quality of a read?

**A**: BioinfUtils uses the phred33 scale.

## License

The MIT License (MIT)

## Contact

Please report any problems directly to the GitHub [issue tracker](https://github.com/aymolokov/bioinf_utils/issues).
Also, you can send your feedback to [a.y.molokov@gmail.com](mailto:a.y.molokov@gmail.com).
