angular.module('studentApp')
.controller('RegisterController', function($scope, $location, $http) {
    $scope.student = {};

    $scope.register = function() {
        $http.post('/api/register', $scope.student)
            .then(function(response) {
                alert('Registration successful!');
                $location.path('/login');
            })
            .catch(function(error) {
                alert(error.data.error || 'Registration failed!');
            });
    };
});