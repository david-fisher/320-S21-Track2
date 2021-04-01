import axios from 'axios';

import { BASE_URL } from '../constants/config';

// Universal fetch request using axios
export default function universalFetch(
    setResponse,
    endpoint,
    onError,
    onSuccess
) {
    setResponse({
        data: null,
        loading: true,
        error: null,
    });
    axios
        .get(BASE_URL + endpoint, {
            headers: {
                studentID: 2
            }
        })
        .then((resp) => {
            setResponse({
                data: resp.data,
                loading: false,
                error: null,
            });
            onSuccess && onSuccess(resp);
        })
        .catch((err) => {
            setResponse({
                data: null,
                loading: false,
                error: err,
            });
            onError && onError(err);
        });
}
