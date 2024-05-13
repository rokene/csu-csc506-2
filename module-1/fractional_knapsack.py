#!/usr/bin/env python3

def fractionalKnapsack(knapsack, itemList, itemListSize) {
   Sort itemList descending by item's (value / weight) ratio
   remaining = knapsack⇢maximumWeight
   for each item in itemList {
      if (item⇢weight <= remaining) {
         Put item in knapsack
         remaining = remaining - item⇢weight
      }
      else {
         fraction = remaining / item⇢weight
         Put (fraction * item) in knapsack
         break
      }
   }
}
