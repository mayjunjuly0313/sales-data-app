import React, { useEffect, useState } from 'react';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from 'recharts';
import Analysis from './Analysis';
import { getChartData } from '../../api/chart-api';

const colors = [
  '#02475e',
  '#810000',
  '#f3bda1',
  '#ff6701',
  '#5b6d5b',
  '#325288',
  '#2978b5',
  '#81b214',
  '#810000',
  '#9e9d89',
  '#fed049',
  '#7eca9c',
  '#890596',
];

function Chart({ form }) {
  const data = useChartData(form);
  const barSize = 5;

  return (
    <>
      {data?.length && (
        <>
          <ResponsiveContainer height='30%'>
            <BarChart
              width={1000}
              height={500}
              data={data}
              margin={{ top: 50, right: 0, left: 100, bottom: 5 }}
            >
              <XAxis
                dataKey={form}
                stroke='#8884d8'
                tick={{ fontSize: 12 }}
                interval={0}
              />
              <YAxis />
              <Tooltip />

              <CartesianGrid stroke='#ccc' strokeDasharray='5 5' />
              {Object.keys(data[0]).map((key, index) => {
                if (key !== 'Region' && key !== 'Item Type') {
                  return (
                    <Bar dataKey={key} fill={colors[index]} barSize={barSize} />
                  );
                }
              })}
              <Legend
                layout='horizontal'
                verticalAlign='top'
                align='right'
                iconSize={8}
              />
            </BarChart>
          </ResponsiveContainer>
          <Analysis form={form} />
        </>
      )}
    </>
  );
}

function useChartData(form) {
  const [chartData, setChartData] = useState();
  const queryForm =
    form === 'Region'
      ? 'products_profit_by_regions'
      : 'regions_profit_by_products';

  const getData = async (queryForm) => {
    const resultData = await getChartData(queryForm);
    setChartData(resultData);
  };

  useEffect(() => {
    getData(queryForm);
  }, []);
  return chartData;
}

export default Chart;
