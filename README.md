# Dice Tools 

Dice tools is a packaged designed for calculating discrete probabilistic distributions 
and their properties for dice based tabletop games such as d6 miniatures games and d20 
RPGs. This quick guide will use a series of examples from the d6 miniatures game from 
[Warhammer 40K](https://warhammer40000.com/) 9th edition. 

## Prerequisites

Dice tools is designed to extend the functionality of [Lea3](https://bitbucket.org/piedenis/lea/src/dev_lea3/). 
Lea3 is a python package for calculating discrete probabilities of all forms. 
Like Lea3, it is recommended that users of Dice Tools also install matplotlib for 
full functionality. Users will find this package most useful if they are also familiar 
with the functionality of Lea3. 

## Installation 
TODO

## Example Use

Often times in dice games players will use the expected value/mean of a roll to analyse
a situation. Alongside mean, this module makes it easy for users to extract data such as 
variance and standard deviation from a probability distribution, as well as to look 
directly at and plot the probability mass function (PMF).

#### Setup

```python
from dice_tools import *
import lea
from lea import leaf 
from lea import P
from lea.leaf import die 
```

#### Re-rolling Dice

Say for example that you would like to know the distribution of success on a roll of 10 six sided 
dice for three different scenarios. In the first scenario a success is defined as any roll of 4 
or greater (4, 5, or 6) is defined as a success. In the second scenario, the same criteria for 
success is defined, except the player may first re-roll any dice with the result of 1 before 
determining success. In the third example the player may re-roll and failed roll (1, 2, or 3) 
before determining the number of successes. The important thing to note here, is that all three
scenarios are defined by [binomial distributions](https://en.wikipedia.org/wiki/Binomial_distribution). 

We can calculate each scenario with the following commands. 
```python
scenario_one = lea.binom(10, P(die() >= 4))
scenario_two = lea.binom(10, P(re_rolling(die(), 1) >= 4))
scenario_three = lea.binom(10, P(re_rolling(die(), [1,2,3]) >= 4))
```

Then we extract information from each object as we would any lea.Lea object. 
```python
(scenario_one.mean, scenario_two.mean, scenario_three.mean)
# -> (5.0, 5.833333333333334, 7.5)
(scenario_one.std, scenario_two.std, scenario_three.std)
# -> (1.5811388300841898, 1.5590239111558089, 1.3693063937629153)
```

#### More Examples
TODO 