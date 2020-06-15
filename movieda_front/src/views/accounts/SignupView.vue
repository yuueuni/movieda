<template>
	<div>
		<h1>Signup</h1>
		<div>
			<label for="username">username: </label>
			<input v-model="loginData.username" id="username" type="text">
		</div>
		<div>
			<label for="password1">password: </label>
			<input v-model="loginData.password" id="password1" type="password">
		</div>
		<div>
			<label for="password2">password: </label>
			<input v-model="loginData.password2" id="password2" type="password">
		</div>
		<div>
			<label for="birthday">birthday: </label>
			<input v-model="loginData.birthday" id="birthday" type="date">
		</div>
		<div>
			<label for="gender">gender: </label>
			<input v-model="loginData.gender" id="gender" type="number">
		</div>
		<div>
			<button @click="signup">signup</button>
		</div>
	</div>
</template>

<script>
export default {
	name: 'LoginView',
		data() {
			return {
					loginData: {
							username: null,
							password1: null,
							password2: null,
							birthday: null,
							gender: null,
					}
				}
			},
			methods: {
				login() {
					this.$emit('submit-signup-data', this.signupData)
				}
		}
	}
</script>

<style>

</style>