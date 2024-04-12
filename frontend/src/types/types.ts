export interface ApiResponse {
  events: Array<Event>
}

export interface Event {
  description: string
  request_id: string
}
