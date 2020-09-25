# nasalis_canine_bodymass_model
This is the mathematical models accounting for the observational data (Matsuda et al. 2020. Commun Biol 3, 522<sup>1</sup>) of canine length and body mass, measured in wild habitat of proboscis monkeys.

<sup>1</sup> Ikki Matsuda, Danica J. Stark, Diana A. Ramirez Saldivar, Augustine Tuuga, Senthilvel K. S. S. Nathan, Benoit Goossens, Carel P. van Schaik and Hiroki Koda. 2020. Large male proboscis monkeys have larger noses but smaller canines. Communications Biology 3, 522. https://doi.org/10.1038/s42003-020-01245-0 (preprint appeared in bioRxiv, 848515. https://www.biorxiv.org/content/10.1101/848515v4. doi: https://doi.org/10.1101/848515)

## Requirements
The code is worked under python3 or anaconda3 with:
- matplotlib3.0.1
- numpy 1.15.2  
- pandas 0.23.4  
- python 3.6.7
- seaborn 0.9.0
- Tested on Mac OS 10.14.6

## Usage
- Main code for the simulation is `nasalis_canine_bodymass_model.py` in the directory `model`.
- Run the following code in your terminal.

```python nasalis_canine_bodymass_model.py```

## Overviews of the simulations
The aim of these simulations was to examine our hypothesis regarding the positive/negative correlations between body mass and canine size<sup>1</sup>. Earlier work distinguished the subadult class from fully adult males based on nasal maturation as well as a fully developed body size. In other words, two developmental stages likely exist among sexually mature males. Therefore, before the acquisition of harem status, subadult males reach a limit in body mass, which cannot increase without a status change. By contrast, in females, the development of body mass and canines is basically similar to that of males before the acquisition of harem status. In this study, we therefore assumed a two-stage model of male development, i.e., a first stage with primary development of body and canine size for both males and females and a second stage that only applies to males and only after the acquisition of harem status.

<sup>2</sup> G. H. Pournelle. Observations on reproductive behaviour and early postnatal development of the Proboscis monkey *Nasalis larvatus* orientalisat San Diego Zoo. International Zoo Yearbook, 7(1): 90–92, 1967. http://doi.wiley.com/10.1111/j.1748-1090.1967.tb00331.x

## Mathematical descriptions
See the main text of our article in bioRxiv. The model part was available in this Github repo as the `model_s.pdf` file in the `tex` directory.

