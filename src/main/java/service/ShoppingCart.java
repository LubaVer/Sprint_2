package service;

import model.Food;

public class ShoppingCart {
    Food[] foods;

    public ShoppingCart(Food[] foods) {
        this.foods = foods;
    }

    public  double getSumShoppingCart() {
        double summ = 0;
        for (Food food : foods) {
            summ += food.getPrice() * food.getAmount();
        }
        return  summ;
    }

    public  double getSumShoppingCartWithDiscount() {
        double summ = 0;
        for (Food food : foods) {
            summ += (food.getPrice() * food.getAmount()) *
                    food.getDiscount();
        }
        return  summ;
    }

    public  double getSumShoppingCartForVegetarian() {
        double summ = 0;
        for (Food food : foods) {
            if (food.isVegetarian()) {
                summ += food.getPrice() * food.getAmount();
            }
        }
        return  summ;
    }

}
