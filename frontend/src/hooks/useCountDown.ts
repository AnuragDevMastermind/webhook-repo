import { useEffect, useState } from "react"

export const useCountDown = (
  initailTime: number,
  callback: () => void,
  interval = 1000
) => {
  const [time, setTime] = useState(initailTime)
  useEffect(() => {
    const customInterval = setInterval(() => {
      if (time > 0) setTime((prev) => prev - interval)
    }, interval)

    if (time === 0) {
      setTime(initailTime)
      callback()
    }

    return () => clearInterval(customInterval)
  }, [time])

  return time
}
