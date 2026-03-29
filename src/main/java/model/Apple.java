package model;


import model.constants.Colour;
import model.constants.Discount;

public class Apple extends Food  {
    String colour;

    public Apple(int amount, double price, String colour){
        isVegetarian = true;
        this.amount = amount;
        this.price = price;
        this.colour = colour;
    }


    @Override
    public double getDiscount() {
        if (this.colour.equals(Colour.red)) {
            return Discount.RED_COLOR;
        }

        return Discount.NO_DISCOUNT;
    }
}
