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
    scenario_stakeHolders: PropTypes.any,
    scenario: PropTypes.number,
    //onChangeStakeholders: PropTypes.any.isRequired,
};

//Needs scenario id
const endpointGET = '/student_info?scenario_id=';

export default function IssueMatrix({ scenario_stakeHolders, scenario }) {
    //receives the scenario ID
    const classes = useStyles();

    const [didGetSHs, setDidGetSHs] = useState(false); //stores status of whether stakeholders have been received
    const stakeHolders = useRef(null);
    //stakeHolders.current = scenario_stakeHolders;
    const [cols, setColumns] = useState([]);
    const [rows, setRows] = useState([]);
    const [issueSums, setSums] = useState([]);

    const [didSetData, setDidSetData] = useState(false);

    const [isLoading, setLoading] = useState(false); //stores status of whether something is loading
    var axios = require('axios'); //backend

    const [successBannerMessage, setSuccessBannerMessage] = useState(''); //success banner
    const [successBannerFade, setSuccessBannerFade] = useState(false);

    useEffect(() => {
        stakeHolders.current = scenario_stakeHolders;
    }, []);

    useEffect(() => {
        if (
            stakeHolders.current !== undefined &&
            stakeHolders.current.length > 0 &&
            didSetData &&
            rows.length === stakeHolders.current.length
        ) {
            onStakeHolderIssueChange();
            //getExistingStakeHolders();
        }
    }, [rows]);

    useEffect(() => {
        if (
            stakeHolders.current !== undefined &&
            stakeHolders.current.length > 0
        ) {
            setColData();
            setRowData();
            setDidSetData(true);
        }
    }, [stakeHolders.current]);

    /*useEffect(() => {
        /*if (didGetSHs) {
            setTimeout(() => {
                if (stakeHolders.current.length > 0) {
                    setDidSetData(true);
                    setColData();
                    setRowData();
                }
           
        }
        //if (stakeHolders.current.length > 0) {
        setTimeout(() => {
            setDidSetData(true);
            setColData();
            setRowData();
        }, 2000);
        //}
    }, [stakeHolders]);*/

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

    function saveStakeHolders() {
        setLoading(true);

        var issues = [];
        var changedStakeHolder;
        for (let i = 0; i < stakeHolders.current.length; i++) {
            let curStakeHolder = stakeHolders.current[i];
            let curRow = rows[i];

            curStakeHolder.issues.forEach((issue) => {
                if (
                    curRow['Issue: ' + issue.name.toUpperCase()] !==
                        issue.coverage_score &&
                    curRow['Decription'] !== 'Total Running Sums'
                ) {
                    issue.coverage_score =
                        curRow['Issue: ' + issue.name.toUpperCase()];
                    changedStakeHolder = curStakeHolder;
                }
                issues.push({
                    COVERAGE_SCORE: issue.coverage_score,
                    ISSUE: issue.issue,
                    STAKEHOLDER: issue.stakeholder,
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
                    changedStakeHolder.stakeholder,
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
                    setLoading(false);
                    setSuccessBannerFade(true);
                })
                .catch(function (error) {
                    setErrorBannerMessage(
                        'Failed to save the issues for this stakeholder! Please try again.'
                    );
                    setErrorBannerFade(true);
                });
        }
        //this.props.onChange(stakeHolders.current);
        setLoading(false);
    }

    function setColData() {
        setLoading(true);
        let cols = [
            { title: 'Name', field: 'NAME' },
            { title: 'Description', field: 'DESCRIPTION' },
        ];
        stakeHolders.current[0].issues.forEach((issue) => {
            let insertBoolean = true;
            for (let i = 0; i < cols.length; i++) {
                if (cols[i].title === 'Issue: ' + issue.name) {
                    insertBoolean = false;
                }
            }
            if (insertBoolean) {
                cols.push({
                    title: 'Issue: ' + issue.name,
                    field: 'Issue: ' + issue.name.toUpperCase(),
                    type: 'numeric',
                });
            }
        });
        setColumns(cols);
        setLoading(false);
    }

    function onStakeHolderIssueChange() {
        let sums = { NAME: '', DESCRIPTION: 'Total Issue Sums' };
        for (let j = 0; j < stakeHolders.current.length; j++) {
            let stakeHolder = stakeHolders.current[j];
            for (let i = 0; i < stakeHolder.issues.length; i++) {
                let curIssue = stakeHolder.issues[i];
                if (
                    sums['Issue: ' + curIssue.name.toUpperCase()] === undefined
                ) {
                    sums['Issue: ' + curIssue.name.toUpperCase()] = 0;
                }
                sums['Issue: ' + curIssue.name.toUpperCase()] +=
                    rows[j]['Issue: ' + curIssue.name.toUpperCase()];
            }
        }
        setSums(sums);
        saveStakeHolders();
    }

    function setRowData() {
        setLoading(true);
        let sums = { NAME: '', DESCRIPTION: 'Total Issue Sums' };
        let data = stakeHolders.current.map((stakeHolder) => {
            let row = {
                name: stakeHolder.name,
                description: stakeHolder.job,
            };
            stakeHolder.issues.forEach((curIssue) => {
                row['Issue: ' + curIssue.name.toUpperCase()] =
                    curIssue.coverage_score;
                if (
                    sums['Issue: ' + curIssue.name.toUpperCase()] === undefined
                ) {
                    sums['Issue: ' + curIssue.name.toUpperCase()] = 0;
                }
                sums['Issue: ' + curIssue.name.toUpperCase()] +=
                    curIssue.coverage_score;
            });
            return row;
        });

        let numPages = Math.ceil(data.length / 10);
        let sumsSpliced = 0;
        for (let i = 0; i < data.length; i++) {
            //always puts a sum row at the ninth index of each page
            if ((i % 10) % 9 == 0 && i !== 0) {
                //gets last digit of i and then checks if ninth index
                data.splice(i, 0, sums);
                sumsSpliced++;
            }
        }
        if (sumsSpliced < numPages) {
            data.push(sums);
        }
        setSums(sums);
        setRows(data);
        setLoading(false);
    }

    function restructureRows(index) {
        for (let i = index; i < rows.length; i++) {
            if (rows[i]['Description'] === 'Total Issue Sums') {
                let temp = rows[i];
                rows[i] = rows[i] + 1;
                rows[i + 1] = temp;
            }
        }
    }

    function deleteStakeHolder(index) {
        setLoading(true);
        let whichPage = 0;
        if (index > 9) {
            whichPage = Math.ceil(index.length + 1 / 10);
        }
        var deletedStakeHolder = stakeHolders.current[index - whichPage - 1];
        restructureRows(index);

        if (deletedStakeHolder !== undefined) {
            stakeHolders.current.splice(index, 1);
            var data = JSON.stringify({});

            var config = {
                method: 'delete',
                url:
                    baseURL +
                    '/api/stakeholders/' +
                    deletedStakeHolder.stakeholder +
                    '/',
                headers: {
                    'Content-Type': 'application/json',
                },
                data: data,
            };

            axios(config)
                .then(function (response) {
                    setSuccessBannerMessage(
                        'Successfully deleted the stakeholder!'
                    );
                    //onChangeStakeHolders();
                    setSuccessBannerFade(true);
                })
                .catch(function (error) {
                    setErrorBannerMessage(
                        'Failed to delete the stakeholder! Please try again.'
                    );
                    setErrorBannerFade(true);
                });
            //this.props.onStakeHolderChange(stakeHolders.current);
        }
        setLoading(false);
    }

    if (isLoading) {
        return <LoadingSpinner />;
    }

    return (
        <Container component="main" className={classes.container}>
            <MaterialTable /*table*/
                icons={tableIcons} /*all the icons*/
                title={'Issue Coverage Matrix'}
                editable={{
                    isEditHidden: (rowData) =>
                        rowData.description === 'Running Issue Sums',
                    isDeleteHidden: (rowData) =>
                        rowData.description === 'Running Issue Sums',
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
                                const dataDelete = [...rows];
                                const index = oldData.tableData.id;
                                dataDelete.splice(index, 1);
                                setRows([...dataDelete]);
                                deleteStakeHolder(index);
                                resolve();
                            }, 1000);
                        }),
                }}
                columns={cols}
                data={rows}
                options={{
                    exportButton: true,
                    pageSize: 10,
                    pageSizeOptions: [10],
                    emptyRowsWhenPaging: false,

                    rowStyle: (rowData) => ({
                        backgroundColor:
                            rows.length === rowData.tableData.id
                                ? '#881c1c'
                                : '#FFF',
                        color:
                            rows.length === rowData.tableData.id
                                ? '#FFF'
                                : '#000000',
                    }),
                    headerStyle: {
                        backgroundColor: '#881c1c',
                        color: '#FFF',
                    },
                }}
            />

            {/* <MaterialTable 
                icons={tableIcons} 
                title={'Running Issue Sums'}
                editable={{
                    isEditHidden: (rowData) =>
                        rowData.DESCRIPTION === 'Running Issue Sums',
                    isDeleteHidden: (rowData) =>
                        rowData.DESCRIPTION === 'Running Issue Sums',
                    onRowUpdate: (newData, oldData) =>
                        new Promise((resolve, reject) => {
                            setTimeout(() => {
                                resolve();
                            }, 1000);
                        }),
                    onRowDelete: (oldData) =>
                        new Promise((resolve, reject) => {
                            setTimeout(() => {
                                resolve();
                            }, 1000);
                        }),
                }}
                columns={[
                    { title: 'Sums', field: 'NAME' },
                    { title: 'Description', field: 'DESCRIPTION' },
                ].concat(cols.slice(2))}
                data={[issueSums]}
                options={{
                    // rowStyle: rowData => ({
                    //     backgroundColor: (rows.length === rowData.tableData.id) ? '#881c1c' : '#FFF',
                    //     color: (rows.length === rowData.tableData.id) ? '#FFF' :'#000000'
                    // }),
                    paging: false,
                    search: false,
                    sorting: false,
                    draggable: false,
                    // showTitle: false,
                    // header: false,
                    headerStyle: {
                        backgroundColor: '#881c1c',
                        color: '#FFF',
                    },
                }}
            /> */}
        </Container>
    );
}
