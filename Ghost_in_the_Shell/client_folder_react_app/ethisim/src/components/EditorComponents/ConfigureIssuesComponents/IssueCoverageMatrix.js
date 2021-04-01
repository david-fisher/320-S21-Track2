import React, { useState, useEffect, useRef } from 'react';
import { makeStyles, withStyles } from '@material-ui/core/styles';
import {
    Container,
    Box,
    Button,
    Typography,
    CssBaseline,
    AppBar,
    Toolbar,
} from '@material-ui/core';
import PropTypes from 'prop-types';
import MaterialTable from 'material-table';
import { forwardRef } from 'react';
import { Link } from 'react-router-dom';
import get from '../../../universalHTTPRequests/get';
import LoadingSpinner from '../../LoadingSpinner';
import SuccessBanner from '../../Banners/SuccessBanner';
import ErrorBanner from '../../Banners/ErrorBanner';
import RefreshIcon from '@material-ui/icons/Refresh';
import ErrorIcon from '@material-ui/icons/Error';
import { useLocation } from 'react-router-dom';
import { baseURL } from '../../../Constants/Config';
import AddBox from '@material-ui/icons/AddBox';
import ArrowDownward from '@material-ui/icons/ArrowDownward';
import Check from '@material-ui/icons/Check';
import ChevronLeft from '@material-ui/icons/ChevronLeft';
import ChevronRight from '@material-ui/icons/ChevronRight';
import Clear from '@material-ui/icons/Clear';
import DeleteOutline from '@material-ui/icons/DeleteOutline';
import Edit from '@material-ui/icons/Edit';
import FilterList from '@material-ui/icons/FilterList';
import FirstPage from '@material-ui/icons/FirstPage';
import LastPage from '@material-ui/icons/LastPage';
import Remove from '@material-ui/icons/Remove';
import SaveAlt from '@material-ui/icons/SaveAlt';
import Search from '@material-ui/icons/Search';
import ViewColumn from '@material-ui/icons/ViewColumn';
import RateReviewIcon from '@material-ui/icons/RateReview';

const tableIcons = {
    Add: forwardRef((props, ref) => <AddBox {...props} ref={ref} />),
    Check: forwardRef((props, ref) => <Check {...props} ref={ref} />),
    Clear: forwardRef((props, ref) => <Clear {...props} ref={ref} />),
    Delete: forwardRef((props, ref) => <DeleteOutline {...props} ref={ref} />),
    DetailPanel: forwardRef((props, ref) => (
        <ChevronRight {...props} ref={ref} />
    )),
    Edit: forwardRef((props, ref) => <Edit {...props} ref={ref} />),
    Export: forwardRef((props, ref) => <SaveAlt {...props} ref={ref} />),
    Filter: forwardRef((props, ref) => <FilterList {...props} ref={ref} />),
    FirstPage: forwardRef((props, ref) => <FirstPage {...props} ref={ref} />),
    LastPage: forwardRef((props, ref) => <LastPage {...props} ref={ref} />),
    NextPage: forwardRef((props, ref) => <ChevronRight {...props} ref={ref} />),
    PreviousPage: forwardRef((props, ref) => (
        <ChevronLeft {...props} ref={ref} />
    )),
    ResetSearch: forwardRef((props, ref) => <Clear {...props} ref={ref} />),
    Search: forwardRef((props, ref) => <Search {...props} ref={ref} />),
    SortArrow: forwardRef((props, ref) => (
        <ArrowDownward {...props} ref={ref} />
    )),
    ThirdStateCheck: forwardRef((props, ref) => (
        <Remove {...props} ref={ref} />
    )),
    ViewColumn: forwardRef((props, ref) => <ViewColumn {...props} ref={ref} />),
    RateReview: forwardRef((props, ref) => (
        <RateReviewIcon {...props} ref={ref} />
    )),
};

const useStyles = makeStyles((theme) => ({
    container: {
        marginTop: theme.spacing(12),
        textAlign: 'center',
    },
    button: {
        marginBottom: theme.spacing(1),
        textTransform: 'unset',
    },
    exitButton: {
        margin: theme.spacing(2),
        borderStyle: 'solid',
        borderColor: 'white',
        border: 2,
    },
    title: {
        textAlign: 'center',
    },
    issue: {
        marginTop: theme.spacing(2),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    errorContainer: {
        marginTop: theme.spacing(2),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    iconError: {
        paddingRight: theme.spacing(2),
        fontSize: '75px',
    },
    iconRefreshLarge: {
        fontSize: '75px',
    },
    iconRefreshSmall: {
        fontSize: '30px',
    },
}));

IssueMatrix.propTypes = {
    stakeHolders: PropTypes.any,
    setStakeHolders: PropTypes.any,
    scenario: PropTypes.number,
};

//Needs scenario id
const endpointGET = '/student_info?scenario_id=';

export default function IssueMatrix({ scenario }) {
    //receives the scenario ID
    const classes = useStyles();

    const [didGetSHs, setDidGetSHs] = useState(false); //stores status of whether stakeholders have been received
    const stakeHolders = useRef(null);
    const [cols, setColumns] = useState([]);
    const [rows, setRows] = useState([]);
    const [issueSums, setSums] = useState([]);

    const [didGetIssues, setDidGetIssues] = useState(false);
    const [didSetData, setDidSetData] = useState(false);

    const [isLoading, setLoading] = useState(false); //stores status of whether something is loading
    var axios = require('axios'); //backend

    const [successBannerMessage, setSuccessBannerMessage] = useState(''); //success banner
    const [successBannerFade, setSuccessBannerFade] = useState(false);

    useEffect(() => {
        stakeHolders.current = [];
    }, []);

    useEffect(() => {
        if (didGetSHs && didSetData) {
            onStakeHolderIssueChange();
        }
    }, [rows]);

    useEffect(() => {
        if (didGetSHs) {
            setTimeout(() => {
                if (stakeHolders.current.length > 0) {
                    setDidSetData(true);
                    setColData();
                    setRowData();
                }
            }, 2000);
        }
    }, [stakeHolders]);

    //let issuePromises = [];

    useEffect(() => {
        //sets behaviour of success banner
        const timeout = setTimeout(() => {
            setSuccessBannerFade(false);
        }, 1000);

        return () => clearTimeout(timeout);
    }, [successBannerFade]);

    const [errorBannerMessage, setErrorBannerMessage] = useState(''); //error banner
    const [errorBannerFade, setErrorBannerFade] = useState(false);

    useEffect(() => {
        //sets behaviour of error banner
        const timeout = setTimeout(() => {
            setErrorBannerFade(false);
        }, 1000);

        return () => clearTimeout(timeout);
    }, [errorBannerFade]);

    function getExistingStakeHolders() {
        //setLoading(true); //starts loading icon

        var data = { SCENARIO: { scenario } };
        var config = {
            method: 'get',
            url: baseURL + '/stakeholder?scenario_id=' + scenario,
            headers: {
                'Content-Type': 'application/json',
            },
            data: data,
        };

        axios(config) //backend call to get data in response
            .then(function (response) {
                stakeHolders.current = stakeHolders.current.concat(
                    response.data
                );
            })
            .catch(function (error) {
                setErrorBannerMessage(
                    'Failed to get Stakeholders! Please try again.'
                );
                setErrorBannerFade(true);
            });
        setDidGetSHs(true);
        setLoading(false);
    }

    function saveStakeHolders() {
        setLoading(true);

        var issues = [];
        var changedStakeHolder;
        for (let i = 0; i < stakeHolders.current.length; i++) {
            let curStakeHolder = stakeHolders.current[i];
            let curRow = rows[i];

            curStakeHolder.ISSUES.forEach((issue) => {
                if (
                    curRow['Issue' + issue.NAME.toUpperCase()] !==
                    issue.COVERAGE_SCORE
                ) {
                    issue.COVERAGE_SCORE =
                        curRow['Issue' + issue.NAME.toUpperCase()];
                    changedStakeHolder = curStakeHolder;
                }
                issues.push({
                    COVERAGE_SCORE: issue.COVERAGE_SCORE,
                    ISSUE: issue.ISSUE,
                    STAKEHOLDER: issue.STAKEHOLDER,
                });
            });
        }

        if (changedStakeHolder !== undefined) {
            var data = [...issues];

            var config = {
                method: 'put',
                url:
                    baseURL +
                    '/multi_coverage?STAKEHOLDER=' +
                    changedStakeHolder.STAKEHOLDER,
                headers: {
                    'Content-Type': 'application/json',
                },
                data: data,
            };

            axios(config)
                .then(function (response) {
                    setSuccessBannerMessage(
                        'Successfully saved the issues for this stakeholder!'
                    );
                    setSuccessBannerFade(true);
                })
                .catch(function (error) {
                    setErrorBannerMessage(
                        'Failed to save the issues for this stakeholder! Please try again.'
                    );
                    setErrorBannerFade(true);
                });
        }
        setLoading(false);
    }

    function setColData() {
        let cols = [
            { title: 'Name', field: 'NAME' },
            { title: 'Description', field: 'DESCRIPTION' },
        ];
        stakeHolders.current[0].ISSUES.forEach((issue) => {
            let insertBoolean = true;
            for (let i = 0; i < cols.length; i++) {
                if (cols[i].title === 'Issue' + issue.NAME) {
                    insertBoolean = false;
                }
            }
            if (insertBoolean) {
                cols.push({
                    title: 'Issue' + issue.NAME,
                    field: 'Issue' + issue.NAME.toUpperCase(),
                    type: 'numeric',
                });
            }
        });
        setColumns(cols);
    }
    function onStakeHolderIssueChange() {
        let sums = { NAME: '', DESCRIPTION: 'Running Issue Sums' };
        for (let j = 0; j < stakeHolders.current.length; j++) {
            let stakeHolder = stakeHolders.current[j];
            for (let i = 0; i < stakeHolder.ISSUES.length; i++) {
                let curIssue = stakeHolder.ISSUES[i];
                if (sums['Issue' + curIssue.NAME.toUpperCase()] === undefined) {
                    sums['Issue' + curIssue.NAME.toUpperCase()] = 0;
                }
                sums['Issue' + curIssue.NAME.toUpperCase()] +=
                    rows[j]['Issue' + curIssue.NAME.toUpperCase()];
            }
        }
        setSums(sums);
        saveStakeHolders();
    }

    function setRowData() {
        setLoading(true);
        let sums = { NAME: '', DESCRIPTION: 'Running Issue Sums' };
        let data = stakeHolders.current.map((stakeHolder) => {
            let row = {
                NAME: stakeHolder.NAME,
                DESCRIPTION: stakeHolder.JOB,
            };
            stakeHolder.ISSUES.forEach((curIssue) => {
                row['Issue' + curIssue.NAME.toUpperCase()] =
                    curIssue.COVERAGE_SCORE;
                if (sums['Issue' + curIssue.NAME.toUpperCase()] === undefined) {
                    sums['Issue' + curIssue.NAME.toUpperCase()] = 0;
                }
                sums['Issue' + curIssue.NAME.toUpperCase()] +=
                    curIssue.COVERAGE_SCORE;
            });
            return row;
        });
        setSums(sums);
        setRows(data);
    }

    if (isLoading) {
        return <LoadingSpinner />;
    }

    if (!didGetSHs) {
        //if stakeholders have alreasdy been loaded, don't do it again
        getExistingStakeHolders();
    }
    /*if (didGetSHs && !didGetIssues) {
        setDidGetIssues(true);
        //getIssues();
    }
    if (didGetIssues && !didSetData) {
        setDidSetData(true);
        setColData();
        setRowData();
    }*/

    return (
        <Container component="main" className={classes.container}>
            <MaterialTable /*table*/
                icons={tableIcons} /*all the icons*/
                title={'Issue Coverage Matrix'}
                options={{
                    exportButton: true,
                }}
                editable={{
                    isEditHidden: (rowData) =>
                        rowData.DESCRIPTION === 'Running Issue Sums',
                    isDeleteHidden: (rowData) =>
                        rowData.DESCRIPTION === 'Running Issue Sums',
                    onRowAdd: (newData) =>
                        new Promise((resolve, reject) => {
                            setTimeout(() => {
                                setRows([...rows, newData]);

                                resolve();
                            }, 1000);
                        }),
                    onRowUpdate: (newData, oldData) =>
                        new Promise((resolve, reject) => {
                            setTimeout(() => {
                                const dataUpdate = [...rows];
                                const index = oldData.tableData.id;
                                dataUpdate[index] = newData;
                                setRows([...dataUpdate]);
                                resolve();
                            }, 1000);
                        }),
                    onRowDelete: (oldData) =>
                        new Promise((resolve, reject) => {
                            setTimeout(() => {
                                /*const dataDelete = [...data];
                                const index = oldData.tableData.id;
                                dataDelete.splice(index, 1);
                                setData([...dataDelete]);*/

                                resolve();
                            }, 1000);
                        }),
                }}
                columns={cols}
                data={rows.concat(issueSums)}
            />
        </Container>
    );
}
