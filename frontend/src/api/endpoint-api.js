import http from "@/utils/http-common"

export default class EndpointApi {
    static create_endpoint(params) {
        return http.post("/endpoint/", params)
    }
    static list_endpoints(params) {
        return http.get('/endpoint', {params: params})
    }
    static get_endpoint(endpoint, params) {
        return http.get('/endpoint/' + endpoint + '/' , {params:params})
    }
}

