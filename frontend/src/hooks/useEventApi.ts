import { useState, useEffect } from "react"
import EventDataService from "../services/event.services"
import { Event } from "../types/types"

export const useEventApi = (defaultTimeStamp: number) => {
  const [data, setData] = useState<Array<Event> | null>(null)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState<Error | null>(null)
  const [timeStamp, setTimeStamp] = useState<number>(defaultTimeStamp)

  const fetchData = async () => {
    setIsLoading(true)
    setData(null) 

    EventDataService.getAll()
      .then((response: any) => {
        console.log(response.data)
        setData(response.data)
      })
      .catch((e: Error) => {
        setError(e)
      })
      .finally(() => {
        setIsLoading(false)
      })
  }

  useEffect(() => {
    fetchData()
  }, [timeStamp]) // Re-fetch only when url changes

  return { data, isLoading, error, setTimeStamp }
}
