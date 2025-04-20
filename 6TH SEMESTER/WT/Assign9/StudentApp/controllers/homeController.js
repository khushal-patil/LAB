angular.module('studentApp')
.controller('HomeController', function($scope, $location, $rootScope) {
    // Check both localStorage and $rootScope for login state
    if (!localStorage.getItem('isLoggedIn') && !$rootScope.isLoggedIn) {
        $location.path('/login');
        return;
    }

    $scope.logout = function() {
        $rootScope.isLoggedIn = false;
        localStorage.removeItem('isLoggedIn');
        $location.path('/login');
    };
});