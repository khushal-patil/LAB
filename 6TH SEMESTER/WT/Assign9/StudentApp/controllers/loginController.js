angular.module('studentApp')
.controller('LoginController', function($scope, $location, $rootScope, $http) {
    $scope.user = {};

    if (localStorage.getItem('isLoggedIn') === 'true') {
        $rootScope.isLoggedIn = true;
        $location.path('/home');
        return;
    }

    $scope.login = function() {
        $http.post('/api/login', $scope.user)
            .then(function(response) {
                $rootScope.isLoggedIn = true;
                localStorage.setItem('isLoggedIn', 'true');
                alert('Login successful!');
                $location.path('/home');
            })
            .catch(function(error) {
                alert(error.data.error || 'Invalid credentials');
            });
    };
});