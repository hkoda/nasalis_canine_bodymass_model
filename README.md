# nasalis_canine_bodymass_model
This is the mathematical models accounting for the observational data (Matsuda et al. 2019 under review or submission) of canine length and body mass, measured in wild habitat of proboscis monkeys.

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
The aim of these simulations was to examine our hypothesis regarding the positive/negative correlations between body mass and canine size. Earlier work distinguished the subadult class from fully adult males based on nasal maturation as well as a fully developed body size. In other words, two developmental stages likely exist among sexually mature males. Therefore, before the acquisition of harem status, subadult males reach a limit in body mass, which cannot increase without a status change. By contrast, in females, the development of body mass and canines is basically similar to that of males before the acquisition of harem status. In this study, we therefore assumed a two-stage model of male development, i.e., a first stage with primary development of body and canine size for both males and females and a second stage that only applies to males and only after the acquisition of harem status.

## Mathematical descriptions
See `model_s.pdf` file in the `tex` directory.

