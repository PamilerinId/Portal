angular.module('b')
    .controller('StudentUploadCtrl', function (Student,toastr) {
        var vm = this;
        vm.uploadStudents = uploadStudents;
        function uploadStudents() {
            for(var i=0; i<vm.students.data.length-1; i++){
                var data = {
                    username: vm.students.data[i][0],
                    last_name: vm.students.data[i][1],
                    first_name: vm.students.data[i][2]+' '+vm.students.data[i][3],
                    dateBirth: vm.students.data[i][4],
                    email: vm.students.data[i][5],
                    sex: vm.students.data[i][6],
                    major: vm.students.data[i][7],
                    level: vm.students.data[i][8],
                    modeOfEntry: vm.students.data[i][9]
                };
                Student.upload(data)
                    .$promise.then(function(){
                    console.log("Done");
                });
            }
        }
    });