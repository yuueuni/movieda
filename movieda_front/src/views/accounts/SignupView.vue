<template>
	<div class="border rounded mx-auto my-3 w-25 bg-light" style="letter-spacing:.5px;">
		<h1 class="my-2">Signup</h1>
    <hr>
		<div class="d-block p-3 mx-auto">
      <div class="input-block w-100">
        <label for="username" class="sr-only">username</label>
        <input v-model="signupData.username" id="username" type="text" class="form-control" placeholder="Username" required autofocus>
      </div>
      <div class="input-block">
        <label for="password1" class="sr-only">password</label>
        <input v-model="signupData.password1" id="password1" type="password" class="form-control" placeholder="Password" required>
      </div>
      <div class="input-block">
        <label for="password2" class="sr-only">password</label>
        <input v-model="signupData.password2" id="password2" type="password" class="form-control" placeholder="Confirm Password" required>
      </div>
      <div>
        <button @click="signup" class="btn btn-primary btn-lg btn-block">Signup</button>
      </div>
    </div>
	</div>
</template>

<script>
export default {
	name: 'SingupView',
	data() {
		return {
			signupData: {
				username: null,
				password1: null,
				password2: null,
				errorMessage: null,
			}
		}
	},
	methods: {
		signup() {
			if (this.signupData.password1.length < 8){
				this.signupData.errorMessage = "비밀번호가 너무 짧습니다."
				alert(this.signupData.errorMessage)
			} else if (this.signupData.password1 !== this.signupData.password2) {
				this.signupData.errorMessage = "비밀번호가 일치하지 않습니다."
				alert(this.signupData.errorMessage)
			}
			else {
				this.$emit('submit-signup-data', this.signupData)
			}
		}
	},
	mounted() {
		this.signupData.errorMessage = null
	}
}
</script>

<style scoped>
.input-block input {
  padding:1.3rem 1rem;
  margin-bottom: 1.5rem;
  font-size: medium;
}
</style>