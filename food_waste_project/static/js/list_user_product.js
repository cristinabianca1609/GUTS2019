function list_user_products(username) {
    $.get('/food_waste_management_app/list_user_products/', {username: username});
    toastr.error('Add new product called!');
};
