const cors = 'https://cors-anywhere.herokuapp.com/'; // use cors-anywhere to fetch api data

$(document).ready(() => {
    $('#form').on('submit', (e) => {
        let x = ($('#lat').val());
        let y = ($('#lng').val());
        let food_type = ($('#f_type').val());
        // console.log(x);
        get_restaurants(x,y,food_type);
        e.preventDefault();
    });
});


function get_restaurants(x,y,foodtype) {
    let radius = 250;
    const API_key = 'AIzaSyAPtgFF8msgOfa_CK_FevErxHxH6HGZ8EM';
    let url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+x+','+y+'&radius='+radius+'&type=restaurant&keyword='+ foodtype+'&key='+API_key;
    //let url = 'http://www.omdbapi.com/?s=danny&apikey=e618da30';
    axios.get(`${cors}${url}`)
            .then((response) => {
            console.log(response);
            let restaurants = response.data.results; //array of resaurants
            let output = '';
            $.each(restaurants, (index, restaurant) => { //get resaurants array. index the resaurant. more on: https://api.jquery.com/jquery.each/
                
                output += `                  
                    <div>
                        <h4>${restaurant.name}</h4>
                        <p>${restaurant.rating}</p>

                    </div>
                `;
            });

            $('#result').html(output);

        })
        .catch((err) => {
            console.log(err);
        });
}
