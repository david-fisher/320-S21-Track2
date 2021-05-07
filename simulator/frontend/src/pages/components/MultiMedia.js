import React, { useState } from "react";
import PropTypes from 'prop-types'

import {
    Typography,
    Box,
    Grid,
    Button,
    makeStyles,
  } from "@material-ui/core";
import HTMLRenderer from './htmlRenderer'

const useStyles = makeStyles((theme) => ({
    mediaBox: {
        margin: 'auto',
        width: 595,
        height: 350,
    },

}));

MultiMedia.defaulProps = {
    name: '',
    description: '',
};

MultiMedia.propTypes = {
    source: PropTypes.string.isRequired,
    name: PropTypes.string,
    description: PropTypes.string,
    height: PropTypes.number,
    type: PropTypes.string.isRequired,
}


export default function MultiMedia({source, name, description, type}) {
    const [showContent, setShowContent] = useState(false);
    const classes = useStyles();
    return (
        <div>
            <Box paddingLeft={0} p={3}>
                <Button 
                    color="primary"
                    disableElevation
                    onClick={() => setShowContent(!showContent)}
                    size="medium"
                >
                    {showContent ? `hide ${type}` : `show ${type}`}
                </Button>
            </Box>
            {
                showContent && 
                <Box mt={3} mb={3} >
                    <Grid container spacing={2} direction="row" justify="space-between" alignItems="stretch">
                        <Grid item xs={7}>
                            {
                                (type === 'link' &&
                                <iframe 
                                    src={source}
                                    frameBorder='0'
                                    className={classes.mediaBox}
                                    allow='autoplay; encrypted-media'
                                    allowfullscreen='true'
                                    title={name}
                                />)
                                ||
                                (type === 'video' &&
                                <video className={classes.mediaBox} controls >
                                    <source src={source} type="video/mp4"/>
                                </video>
                                )
                                ||
                                (type === 'image' &&
                                <img src={source} className={classes.mediaBox}/>
                                )
                                ||
                                (type === 'audio' &&
                                <audio width={595} controls>
                                    <source src={source} type="audio/mpeg"/>
                                </audio>
                                )
                            }
                        </Grid>
                        <Grid item xs={4}>
                                <Typography variant="h6">
                                    {name}
                                </Typography>
                                <HTMLRenderer html={description}/>
                        </Grid>
                    </Grid>
                </Box>
            }
        </div>
    );
}

