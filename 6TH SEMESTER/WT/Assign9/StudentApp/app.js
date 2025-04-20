angular.module('studentApp', ['ngRoute'])
.config(function($routeProvider) {
    $routeProvider
    .when('/login', {
        templateUrl: 'views/login.html',
        controller: 'LoginController'
    })
    .when('/register', {
        templateUrl: 'views/register.html',
        controller: 'RegisterController'
    })
    .when('/home', {
        templateUrl: 'views/home.html',
        controller: 'HomeController'
    })
    .otherwise({
        redirectTo: '/login'
    });
})
.run(function($rootScope) {
    // Initialize login state from localStorage
    $rootScope.isLoggedIn = localStorage.getItem('isLoggedIn') === 'true';
});;