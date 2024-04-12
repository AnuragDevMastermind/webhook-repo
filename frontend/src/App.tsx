import "bootstrap/dist/css/bootstrap.css"
import { Table } from "react-bootstrap"
import "./App.css"
import { useEventApi } from "./hooks/useEventApi"
import { Event } from "./types/types"
import { useCountDown } from "./hooks/useCountDown"

const App = () => {
  const { data, isLoading, error, setTimeStamp } = useEventApi(
    new Date().getTime()
  )
  const time = useCountDown(15 * 1000, () => setTimeStamp(new Date().getTime()))

  if (isLoading) {
    return <div>Loading...</div>
  }

  if (error) {
    return <div>Error: {error.message}</div>
  }

  if (data == null) {
    return <div>Data is null</div>
  }

  if (!data) {
    return <div>Data is null or events are undefined</div>
  }

  return (
    <>
      <h1 style={{ textAlign: "center" }}>00: {time < 10000 ? `0${time / 1000}` : `${time / 1000}`}</h1>
      <Table>
        <thead>
          <tr>
            <th>S.No</th>
            <th>Request Id</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          {data.map((event: Event, index: number) => (
            <tr key={index}>
              <td>{index+1}</td>
              <td>{event.request_id}</td>
              <td>{event.description}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </>
  )
}

export default App
