import React, {useState, useEffect} from 'react'
import {Button, Box} from "@material-ui/core";

export default function AudioPlayer({source}) {
    const [audio] = useState(new Audio(source))
    const [playing, setPlaying] = useState(false)

    const reset = () => {
        audio.load()
        playing && setPlaying(!playing)
    }

    useEffect(() => {
        playing ? audio.play() : audio.pause();
      },
      [playing]
    );

    return (
        <div>
            <Box paddingLeft={0} p={2}>
                <Button 
                    color="primary"
                    variant="contained"
                    disableElevation
                    onClick={() => setPlaying(!playing)}
                    size="large"
                >
                    {playing ? "Pause" : "Play"}
                </Button>
            </Box>
            <Box paddingLeft={0} p={2}>
                <Button 
                color="primary"
                variant="contained"
                disableElevation
                onClick={() => reset()}
                size="large"
                >
                    reset
                </Button>
            </Box>
        </div>
    )
}