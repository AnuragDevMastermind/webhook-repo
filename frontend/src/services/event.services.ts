import http from "../http-common";
import { Event } from "../types/types";

class EventDataService {
    getAll() {
        return http.post<Array<Event>>("/event/all");
    }
}

export default new EventDataService();