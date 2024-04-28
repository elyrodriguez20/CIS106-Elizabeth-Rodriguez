def sales_forecast(month, sales):
  if month== "jan" or month== "feb" or month== "mar":
    forecast= sales * 1.1
  elif month== "apr" or month== "may" or month== "jun":
    forecast= sales * 1.15
  elif month== "jul" or month== "aug" or month== "sep":
    forecast= sales * 1.2
  elif month== "oct" or month== "nov" or month== "dec":
    forecast= sales * 1.25
  return forecast


def saquare_footage( length, width, height):
  sf= 2*width*height + 2* length*height +2* width*length
  return sf

def discount_prices(price, discount):
  discamount= price * discount
  discprice= price - discamount
  return discprice