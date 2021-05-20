<template>
  <div class="endpoint-detail" v-if="endpoint">
    <div class="endpoint">
      <div class="title" id="title">{{ base_url + endpoint.endpoint_suffix + '/' }}</div>
      <div class="sub-details">
        <span class="tag">Expires {{ getTime(endpoint.created) }}</span>
        <button @click="copy" class="copy-button">Copy</button>
      </div>
    </div>
    <section class="activity-section">
      <div v-for="(activity,index) in endpointActivity" class="activity-wrapper" :key="index">
        <span class="expiry">Expires {{ activity.created | moment('from', 'now') }}</span>
        <div class="sub-title">METHOD - <span class="method">{{ activity.data.method }}</span></div>
        <div class="sub-title">
          Query Params
        </div>
        <vue-json-pretty  v-if="Object.keys(activity.data.query_params).length" :data="activity.data.query_params"> </vue-json-pretty>
        <div class="nil" v-else>NIL</div>
        <div class="sub-title">
          Data
        </div>
        <vue-json-pretty  v-if="Object.keys(activity.data.data).length" :data="activity.data.data"> </vue-json-pretty>
        <div class="nil" v-else>NIL</div>
        <div class="sub-title">
          Headers
        </div>
        <vue-json-pretty  v-if="Object.keys(activity.headers).length" :data="activity.headers"> </vue-json-pretty>
        <div class="nil" v-else>NIL</div>
      </div>
    </section>
  </div>
</template>

<script>
import EndpointApi from "../api/endpoint-api";
import VueJsonPretty from 'vue-json-pretty';
import 'vue-json-pretty/lib/styles.css';


export default {
  name: 'endpoint-detail',
  components: {
    VueJsonPretty
  },
  data() {
    return {
      endpoint: null,
      endpointActivity: null,
      base_url: ''
    }
  },
  methods: {
    getTime(created) {
      let m_created = this.$moment(created)
      let expiry = this.$moment(m_created).add(1, 'hours')
      console.log(expiry.unix() - m_created.unix())
      console.log(m_created.toString())
      console.log(expiry.toString())
      console.log(expiry.from(this.$moment()))
      return expiry.from(this.$moment())
    },
    copy() {
      let url = document.querySelector('#title').textContent
      this.copyToClipBoard(url)

    },
    copyToClipBoard(str) {
      const el = document.createElement('textarea');
      el.value = str;
      document.body.appendChild(el);
      el.select();
      document.execCommand('copy');
      document.body.removeChild(el);
      alert('copied url')
    }
  },
  created() {
    if ('endpoint' in this.$route.params) {
      EndpointApi.get_endpoint(this.$route.params.endpoint,).then(response => {
        this.endpoint = response.data.endpoint
        this.endpointActivity = response.data.endpoint_activity
        this.base_url = response.data.base_url
      })
    }
  }
}
</script>

<style lang="css">
.endpoint-detail {
  padding: 30px 20px;
  height: 100%;
  text-align: left;
}

.endpoint {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: nowrap;
  background: lightblue;
  padding: 10px 7px;
}

.endpoint .sub-details {
  padding-right: 30px;
}

.sub-details .tag {
  border-radius: 3px;
  padding: 7px 5px;
  margin-right: 30px;
  color: black;
  background: cornflowerblue;
}

.endpoint .title {
  width: fit-content;
  max-width: 65%;
  padding: 5px;
  font-size: 18px;
  font-weight: 600;
}

.tag {
  font-size: 15px;
  font-weight: 500;
}

.copy-button {
  border: none;
  border-radius: 3px;
  background: lightseagreen;
  font-size: 14px;
  text-transform: uppercase;
  padding: 7px 12px;
  transition: box-shadow 0.3s ease-in-out;
}

.copy-button:hover {
  outline: none;
}

.copy-button:hover {
  background: #087972;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
}
.activity-section{
  padding-top: 20px;
  position: relative;
  max-height: 85%;
  overflow-y: scroll;
}
.expiry {
  position: absolute;
  right: 10px;
  font-size: 14px;
  font-weight: 500;
  color: darkslategray;
}
.activity-wrapper{
  margin-bottom: 30px;
  padding: 10px 7px;
  background: lightslategrey;
  overflow-x: scroll;
}
.sub-title{
  font-weight: 700;
  font-size: 14px;
  padding-bottom: 5px;
  text-transform: uppercase;
}
.nil {
  padding-bottom: 16px;
}
.sub-title:first-child{
  padding-bottom: 20px;
}
</style>