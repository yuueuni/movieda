<template>
  <div>
    <div class="border rounded mx-auto my-3 w-25 bg-light" style="letter-spacing:.5px;">
      <h1 class="my-2">Login</h1>
      <hr>
      <div class="d-block p-3 mx-auto">
        <div class="input-block w-100">
          <label for="username" class="sr-only">username</label>
          <input v-model="loginData.username" id="username" type="text" class="form-control" placeholder="Username" required autofocus>
        </div>
        <div class="input-block">
          <label for="password" class="sr-only">password</label>
          <input v-model="loginData.password" id="password" type="password" class="form-control" placeholder="Password" required>
        </div>
        <div>
          <button @click="login" class="btn btn-primary btn-lg btn-block">Login</button>
        </div>
      </div>
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
								password: null,
            }
        }
    },
    methods: {
        login() {
					this.$emit('submit-login-data', this.loginData)
        }
		},
		created() {
			if (this.$cookies.isKey('auth-token')){
				this.$router.push({ name:'Home'})
			}
		}
}
</script>

<style>
.input-block input {
  padding: 1.3rem 1rem;
  margin-bottom: 1.5rem;
  font-size: medium;
}
</style>