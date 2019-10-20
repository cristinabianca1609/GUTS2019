//function removebookmark(concertid) {
//    $.get('/concert/removebookmark/', {concertid: concertid});
//    toastr.error('Bookmark removed!');
//};

function add_new_product(username) {
    $.get('/food_waste_management_app/add_new_product/', {username: username});
    toastr.error('Add new product called!');
};
