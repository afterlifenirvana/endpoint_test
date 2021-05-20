<template>
  <section class="home">
    <div class="title">
      <div>Endpoint Inspector</div>
      <span>Create endpoints and inspect data posted on to them in a user friendly way.</span>
    </div>
    <div class="button-wrapper">
      <button class="button" @click="createEndpoint">Create Endpoint</button>
    </div>
    <div class="endpoint-list">
      <div v-for="(endpoint, index) in endpoint_list" class="card" :key="index">
        <div class="card-title" >
          <router-link :to="{'name': 'endpoint-detail', params: {endpoint: endpoint.id}}">{{ endpoint.endpoint_suffix }}</router-link>
        </div>
        <div class="details">
          <div>
            Expires {{ getTime(endpoint.created) }}
          </div>
          <div>
            Used {{ endpoint.hits }} times in last 5 mins
          </div>
        </div>
      </div>
    </div>
    <!--    <modal height="auto" class="endpoint-create-modal" name="endpoint-create">-->
    <!--      <section class="modal-box">-->
    <!--        <input v-model="endpoint">-->
    <!--        <button @click="createEndpoint">Submit</button>-->
    <!--      </section>-->
    <!--    </modal>-->
  </section>
</template>

<script>
// @ is an alias to /src
import EndpointApi from "../api/endpoint-api";

export default {
  name: 'Home',
  components: {},
  data() {
    return {
      endpoint: '',
      endpoint_list: [],
    }
  },
  methods: {
    createEndpoint() {
      EndpointApi.create_endpoint().then(response => {
        if (response.status === 201) {
          this.endpoint = ''
          this.getEndpoints()
        }
      })
      // this.closeModal()
    },
    // openModal() {
    //   this.$modal.show('endpoint-create')
    // },
    // closeModal() {
    //   this.$modal.hide('endpoint-create')
    // },
    getTime(created) {
      let m_created = this.$moment(created)
      let expiry = this.$moment(m_created).add(1, 'hours')
      console.log(expiry.unix() - m_created.unix())
      console.log(m_created.toString())
      console.log(expiry.toString())
      console.log(expiry.from(this.$moment()))
      return expiry.from(this.$moment())
    },
    getEndpoints() {
      EndpointApi.list_endpoints({}).then(response => {
        this.endpoint_list = response.data.results
      })
    }
  },
  created() {
    this.getEndpoints()
  }
}
</script>

<style lang="css">
.home {
  padding: 30px 40px;
  height: 100%;
}

.title {
  text-align: left;
  font-size: 24px;
  font-weight: 700;
}

.title span {
  font-size: 12px;
}

.button-wrapper {
  margin: 20px;
}

.button {
  border-radius: 3px;
  padding: 16px 20px;
  font-size: 18px;
  color: white;
  background: #18be18;
  border: none;
  transition: box-shadow 0.3s ease-in-out;
}

.button:focus {
  border: none;
}

.button:hover {
  outline: none;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3);

}

.modal-box {
  padding: 20px 0;
}

.endpoint-list {
  display: flex;
  flex-wrap: wrap;
  min-height: 70%;
  max-height: 70%;
}

.card {
  padding: 20px 15px;
  border: 1px solid slategrey;
  border-radius: 2px;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
  height: fit-content;
  margin-right: 20px;
  max-width: 250px;
}
.card-title {
  padding-bottom: 16px;
}
.card .card-title a {
  font-size: 16px;
  font-weight: 500;
  color: #5f9ea0;
  cursor: pointer;
  text-decoration: none;
}
.card-title a:hover {
  color: #126d6e;
}
</style>