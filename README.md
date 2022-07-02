# Coffee Calculator

Convert Barista Hustle style recipes with diluted solutions to non-diluted recipes that allow you to directly add the solute into the distilled water instead of creating the buffer and mg solutions. 

## How to Use

`python coffee.py --name coffee --buffer 50.1 --mg=75.7 --water=874.2 --output=500`

In this case the name is coffee, the original recipe uses 50.1 ml of buffer, 75.7 ml of mg and 874.2 ml of water. We are requesting a new recipe that is based on 500.0 ml of water.

```log
coffee: 
    nahco3 0.56g 
    mgs04  1.23g 
    water  500.0g
```

This is the output which provides a new recipe which requres 0.56g of baking soda and 1.23g of epsom salts combined with 500g of DI water.
