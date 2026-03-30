import model.Apple;
import model.Food;
import model.Meat;
import model.constants.Colour;
import service.ShoppingCart;

public class Main {
    public static void main(String[] args) {
        Food meat = new Meat(5, 100);
        Food redApple = new Apple(10,50, Colour.RED);
        Food greenApple = new Apple(8,60, Colour.GREEN);
        Food[] products = {meat, redApple,greenApple};

        ShoppingCart myCart = new ShoppingCart(products);



        System.out.printf("Общая сумма товаров без скидки: %.2f\n",  myCart.getSumShoppingCart());
        System.out.printf("Общая сумма товаров со скидкой: %.2f\n", myCart.getSumShoppingCartWithDiscount());
        System.out.printf("Сумма всех вегетарианских продуктов без скидки: %.2f\n", myCart.getSumShoppingCartForVegetarian());


    }
}
