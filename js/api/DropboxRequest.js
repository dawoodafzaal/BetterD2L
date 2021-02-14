import Request from './Request';

class DropboxRequest extends Request{
    retrieve() {
        return this.get('http://127.0.0.1:5000/dropboxes');
    }

    destroy(id) {
        return this.delete('http://127.0.0.1:5000/dropboxes/' + id);
    }
}

export default DropboxRequest