select milk.cart_id
from (
    select cart_id
    from cart_products
    where name = 'Milk'
) as milk
join (
    select cart_id
    from cart_products
    where name = 'Yogurt'
) yogurt
on milk.cart_id = yogurt.cart_id
order by milk.cart_id