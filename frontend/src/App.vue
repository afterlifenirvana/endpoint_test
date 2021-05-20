<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style>
@import url("https://fonts.googleapis.com/css?family=Inter:100,200,300,400,500,600,700,800,900&display=swap");
html, body {
  width: 100%;
  height: 100%;
}
#app {
  font-family: 'Oswald', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
