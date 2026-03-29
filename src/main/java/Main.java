import model.Apple;
import model.Food;
import model.Meat;
import model.constants.Colour;
import service.ShoppingCart;

public class Main {
    public static void main(String[] args) {
        Food meat = new Meat(5, 100);
        Food redApple = new Apple(10,50, Colour.red);
        Food greenApple = new Apple(8,60, Colour.green);
        Food[] products = {meat, redApple,greenApple};

        ShoppingCart myCart = new ShoppingCart(products);



        System.out.println("Общая сумма товаров без скидки " + myCart.getSumShoppingCart());
        System.out.println("Общая сумма товаров со скидкой " + myCart.getSumShoppingCartWithDiscount());
        System.out.println("Сумма всех вегетарианских продуктов без скидки " +
                myCart.getSumShoppingCartForVegetarian());


    }
}
