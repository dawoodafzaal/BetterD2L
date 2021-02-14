import Errors from './Errors.js';
import axios from 'axios';

class Request {
    constructor(fields) {
        this.setFields(fields);
        this.setContentType('application/json');
    }

    setContentType(contentType)
    {
        this.contentType = contentType;
    }

    setFields(fields) {
        this.fieldData = fields;

        for(let field in fields) {
            this[field] = fields[field];
        }

        this.errors = new Errors();
    }

    data() {
        let data = {};

        for(let field in this.fieldData) {
            data[field] = this[field];
        }

        return data;
    }

    get(url){
        return this.submit('get' , url);
    }

    patch(url){
        return this.submit('patch' , url);
    }

    post(url){
        return this.submit('post' , url);
    }

    put(url){
        return this.submit('put' , url);
    }

    delete(url){
        return this.submit('delete' , url);
    }

    submit(request , url) {
        return new Promise((resolve, reject) => {
            axios[request](url , this.data(), {
                headers: {
                    'Content-Type': this.contentType
                }
            })
            .then(response => {
                this.onSuccess();

                resolve(response.data);
            })
            .catch(error => {
                this.onFail(error.response.data.errors);

                reject(error.response.data);
            });
        });
    }

    clear() {
        for(let field in this.fieldData) {
            this[field] = '';
        }

        this.errors.clear();
    }

    onSuccess() {
        this.clear();
    }

    onFail(errors) {
        this.errors.record(errors);
    }
}

export default Request