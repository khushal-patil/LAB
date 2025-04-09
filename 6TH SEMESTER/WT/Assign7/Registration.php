<?php
$con = mysqli_connect("localhost", "root", "", "registration") or die(mysqli_error($con));

if ($con) {
	echo "connected...";
}

$edit_mode = false;
$id = $fname = $mname = $lname = $address = $email = $state = $district = $city = $gender = $dob = $mobile = $branch = "";
$qualification = [];

// Delete
if (isset($_GET['id'])) {
	$del = mysqli_query($con, "DELETE FROM register WHERE id='" . $_GET['id'] . "'");
	if ($del == 1) {
		echo "<script>alert('Record Deleted...'); location.href = 'Registration.php';</script>";
	}
}

// Edit Fetch
if (isset($_GET['edit'])) {
	$edit_mode = true;
	$id = $_GET['edit'];
	$result = mysqli_query($con, "SELECT * FROM register WHERE id='$id'");
	$row = mysqli_fetch_array($result);

	$fname = $row['fname'];
	$mname = $row['mname'];
	$lname = $row['lname'];
	$address = $row['address'];
	$email = $row['email'];
	$state = $row['state'];
	$district = $row['district'];
	$city = $row['city'];
	$gender = $row['gender'];
	$dob = $row['dob'];
	$mobile = $row['mobile'];
	$branch = $row['branch'];
	$qualification = explode(",", rtrim($row['qualification'], ","));
}

// Insert or Update
if (isset($_POST['SubmitBtn'])) {
	extract($_POST);
	$qualify1 = "";
	foreach ($_POST['qualification'] as $choice) {
		$qualify1 .= $choice . ",";
	}

	if (!empty($_POST['id'])) {
		$update = mysqli_query($con, "UPDATE register SET fname='$fname', mname='$mname', lname='$lname', address='$address', email='$email', state='$state', district='$district', city='$city', gender='$gender', dob='$dob', mobile='$mobile', branch='$branch', qualification='$qualify1' WHERE id='" . $_POST['id'] . "'") or die(mysqli_error($con));
		if ($update == 1) {
			echo "<script>alert('Record Updated...'); location.href = 'Registration.php';</script>";
		}
	} else {
		$insert = mysqli_query($con, "INSERT INTO register(fname, mname, lname, address, email, state, district, city, gender, dob, mobile, branch, qualification)
            VALUES('$fname', '$mname', '$lname', '$address', '$email', '$state', '$district', '$city', '$gender', '$dob', '$mobile', '$branch', '$qualify1')") or die(mysqli_error($con));
		if ($insert == 1) {
			echo "<script>alert('Record Inserted...'); location.href = 'Registration.php';</script>";
		}
	}
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<title>Registration & Display</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>

<body class="bg-light">

	<div class="container py-4" style="max-width: 1500px;">
		<div class="card shadow mb-5">
			<div class="card-header bg-<?= $edit_mode ? 'primary' : 'success' ?> text-white">
				<h4 class="mb-0"><?= $edit_mode ? "Update" : "Registration" ?> Form</h4>
			</div>
			<div class="card-body">
				<form method="post" autocomplete="off">
					<input type="hidden" name="id" value="<?= $edit_mode ? $id : '' ?>">

					<div class="row mb-3">
						<div class="col-md-4"><input type="text" class="form-control" name="fname"
								placeholder="First Name" value="<?= $fname ?>"></div>
						<div class="col-md-4"><input type="text" class="form-control" name="mname"
								placeholder="Middle Name" value="<?= $mname ?>"></div>
						<div class="col-md-4"><input type="text" class="form-control" name="lname"
								placeholder="Last Name" value="<?= $lname ?>"></div>
					</div>
					<div class="mb-3">
						<textarea class="form-control" name="address" placeholder="Address"><?= $address ?></textarea>
					</div>
					<div class="mb-3">
						<input type="email" class="form-control" name="email" placeholder="Email" value="<?= $email ?>">
					</div>

					<div class="row mb-3">
						<div class="col-md-4">
							<select class="form-select" name="state">
								<option>Select State</option>
								<?php
								$states = ['Gujrat', 'Maharashtra', 'Delhi', 'West Bengal', 'Kerala'];
								foreach ($states as $s) {
									$sel = $state == $s ? 'selected' : '';
									echo "<option $sel>$s</option>";
								}
								?>
							</select>
						</div>
						<div class="col-md-4">
							<select class="form-select" name="district">
								<option>Select District</option>
								<?php
								$districts = ['Dhule', 'Nashik', 'Jalgaon', 'Thane', 'Pune'];
								foreach ($districts as $d) {
									$sel = $district == $d ? 'selected' : '';
									echo "<option $sel>$d</option>";
								}
								?>
							</select>
						</div>
						<div class="col-md-4"><input type="text" class="form-control" name="city" placeholder="City"
								value="<?= $city ?>"></div>
					</div>

					<div class="row mb-3">
						<div class="col-md-4">
							<label class="form-label">Gender:</label><br>
							<div class="form-check form-check-inline">
								<input class="form-check-input" type="radio" name="gender" value="Male"
									<?= $gender == "Male" ? 'checked' : '' ?>>
								<label class="form-check-label">Male</label>
							</div>
							<div class="form-check form-check-inline">
								<input class="form-check-input" type="radio" name="gender" value="Female"
									<?= $gender == "Female" ? 'checked' : '' ?>>
								<label class="form-check-label">Female</label>
							</div>
						</div>
						<div class="col-md-4"><input type="date" class="form-control" name="dob" value="<?= $dob ?>">
						</div>
						<div class="col-md-4"><input type="tel" class="form-control" name="mobile"
								placeholder="Mobile No." value="<?= $mobile ?>"></div>
					</div>

					<div class="row mb-3">
						<div class="col-md-6">
							<select class="form-select" name="branch">
								<option>Select Branch</option>
								<?php
								$branches = ['Computer Engg.', 'Mechanical Engg.', 'Civil Engg.', 'ENTC Engg.'];
								foreach ($branches as $c) {
									$sel = $branch == $c ? 'selected' : '';
									echo "<option $sel>$c</option>";
								}
								?>
							</select>
						</div>
						<div class="col-md-6">
							<label class="form-label">Qualification:</label>
							<?php
							$quals = ['10th', '12th', 'Diploma'];
							foreach ($quals as $q) {
								$chk = in_array($q, $qualification) ? 'checked' : '';
								echo "<div class='form-check form-check-inline'>
                                    <input class='form-check-input' name='qualification[]' type='checkbox' value='$q' $chk>
                                    <label class='form-check-label'>$q</label>
                                </div>";
							}
							?>
						</div>
					</div>

					<div class="text-center">
						<button class="btn btn-<?= $edit_mode ? 'primary' : 'success' ?>" name="SubmitBtn"
							type="submit">
							<?= $edit_mode ? 'Update' : 'Submit' ?>
						</button>
					</div>
				</form>
			</div>
		</div>

		<div class="card shadow">
			<div class="card-header bg-dark text-white">
				<h4 class="mb-0">Submitted Data</h4>
			</div>
			<div class="card-body table-responsive">
				<table class="table table-bordered table-striped">
					<thead class="table-light text-center">
						<tr>
							<th>Sr No</th>
							<th>First</th>
							<th>Middle</th>
							<th>Last</th>
							<th>Address</th>
							<th>Email</th>
							<th>State</th>
							<th>District</th>
							<th>City</th>
							<th>Gender</th>
							<th>DOB</th>
							<th>Mobile</th>
							<th>branch</th>
							<th>Qualification</th>
							<th>Actions</th>
						</tr>
					</thead>
					<tbody class="text-center">
						<?php
						$result = mysqli_query($con, "SELECT * FROM register");
						if (mysqli_num_rows($result) == 0) {
							echo "<tr><td colspan='15'>No Records Found</td></tr>";
						} else {
							$sr = 1;
							while ($row = mysqli_fetch_array($result)) {
								echo "<tr>";
								echo "<td>$sr</td><td>{$row['fname']}</td><td>{$row['mname']}</td><td>{$row['lname']}</td><td>{$row['address']}</td><td>{$row['email']}</td>";
								echo "<td>{$row['state']}</td><td>{$row['district']}</td><td>{$row['city']}</td><td>{$row['gender']}</td><td>{$row['dob']}</td>";
								echo "<td>{$row['mobile']}</td><td>{$row['branch']}</td><td>{$row['qualification']}</td>";
								echo "<td>
                            <a href='Registration.php?edit={$row['id']}' class='btn btn-sm btn-outline-primary'>Edit</a>
                            <a href='Registration.php?id={$row['id']}' class='btn btn-sm btn-outline-danger' onclick=\"return confirm('Are you sure to delete?')\">Delete</a>
                        </td>";
								echo "</tr>";
								$sr++;
							}
						}
						?>
					</tbody>
				</table>
			</div>
		</div>
	</div>

</body>

</html>