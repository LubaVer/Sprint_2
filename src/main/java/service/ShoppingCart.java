package service;

import model.Food;

public class ShoppingCart {
    Food[] foods;

    public ShoppingCart(Food[] foods) {
        this.foods = foods;
    }

    public  double getSumShoppingCart() {
        double summ = 0;
        for (int i = 0; i < foods.length; i++) {
            summ += this.foods[i].getPrice() * this.foods[i].getAmount();
        }
        return  summ;
    }

    public  double getSumShoppingCartWithDiscount() {
        double summ = 0;
        for (int i = 0; i < foods.length; i++) {
            summ += (this.foods[i].getPrice() * this.foods[i].getAmount()) * this.foods[i].getDiscount();
        }
        return  summ;
    }

    public  double getSumShoppingCartForVegetarian() {
        double summ = 0;
        for (int i = 0; i < foods.length; i++) {
            if (this.foods[i].isVegetarian()) {
                summ += this.foods[i].getPrice() * this.foods[i].getAmount();
            }
        }
        return  summ;
    }

}
