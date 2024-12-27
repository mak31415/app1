// Когда html документ готов (прорисован)
$(document).ready(function () {

    // берем в переменную элемент разметки с id jq-notification для оповещений от ajax
    var successMessage = $("#jq-notification");

    // Ловим собыитие клика по кнопке добавить в корзину
    $(document).on("click", ".add-to-cart", function (e) {
        // Блокируем его базовое действие
        e.preventDefault();

        // Берем элемент счетчика в значке корзины и берем оттуда значение
        var goodsInCartCount = $("#goods-in-cart-count");
        var cartCount = parseInt(goodsInCartCount.text() || 0);

        // Получаем id товара из атрибута data-product-id
        var product_id = $(this).data("product-id");

        // Из атрибута href берем ссылку на контроллер django
        var add_to_cart_url = $(this).attr("href");

        // делаем post запрос через ajax не перезагружая страницу
        $.ajax({
            type: "POST",
            url: add_to_cart_url,
            data: {
                product_id: product_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                // Сообщение
                successMessage.html(data.message);
                successMessage.fadeIn(400);
                // Через 7сек убираем сообщение
                setTimeout(function () {
                    successMessage.fadeOut(400);
                }, 7000);

                // Увеличиваем количество товаров в корзине (отрисовка в шаблоне)
                cartCount++;
                goodsInCartCount.text(cartCount);

                // Меняем содержимое корзины на ответ от django (новый отрисованный фрагмент разметки корзины)
                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);

            },

            error: function (data) {
                console.log("Ошибка при добавлении товара в корзину");
            },
        });
    });

  // Берем из разметки элемент по id - оповещения от django
  var notification = $('#notification');
  // И через 7 сек. убираем
  if (notification.length > 0) {
      setTimeout(function () {
          notification.alert('close');
      }, 7000);
  }

  // При клике по значку корзины открываем всплывающее(модальное) окно
  $('#modalButton').click(function () {
      $('#exampleModal').appendTo('body');

      $('#exampleModal').modal('show');
  });

  // Собыите клик по кнопке закрыть окна корзины
  $('#exampleModal .btn-close').click(function () {
      $('#exampleModal').modal('hide');
  });

  // Обработчик события радиокнопки выбора способа доставки
  $("input[name='requires_delivery']").change(function() {
      var selectedValue = $(this).val();
      // Скрываем или отображаем input ввода адреса доставки
      if (selectedValue === "1") {
          $("#deliveryAddressField").show();
      } else {
          $("#deliveryAddressField").hide();
      }
  });
  
});