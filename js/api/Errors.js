class Errors {
    constructor() {
        this.errors = { };
    }

    has(field) {
        return this.errors.hasOwnProperty(field);
    }

    get(field) {
        return this.errors[field];
    }

    record(errors) {
        this.errors = errors;
    }

    any() {
        return Object.keys(this.errors).length > 0;
    }

    clear(field) {
        if(field) {
            delete this.errors[field];

            return;
        }

        this.errors = {};
    }
}

export default Errors;