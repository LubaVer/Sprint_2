package model;

import static model.constants.Discount.NO_DISCOUNT;

public abstract class Food implements Discountable {
    protected int amount;
    protected double price;
    protected boolean isVegetarian;

    public int getAmount() {
        return amount;
    }

    public double getPrice() {
        return price;
    }

    public boolean isVegetarian(){
        return isVegetarian;
    }

    @Override
    public double getDiscount() {
        return NO_DISCOUNT;
    }

}
