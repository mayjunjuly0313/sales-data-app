import React, { useEffect, useState } from 'react';
import { getAnalysisData } from '../../api/analysis-api';

function Analysis({ form }) {
  const min_max_profit = useMinMaxProfitData(form);

  return (
    <>
      {min_max_profit && (
        <div style={{ textAlign: 'left', marginLeft: '10vw' }}>
          <p>
            The Most Profitable {form}:{' '}
            <span style={{ color: 'red' }}>{min_max_profit['max']} </span>
          </p>

          <p>
            The Least Profitable {form}:{' '}
            <span style={{ color: 'blue' }}>{min_max_profit['min']}</span>
          </p>
        </div>
      )}
    </>
  );
}

function useMinMaxProfitData(form) {
  const [analysisData, setAnalysisData] = useState();

  const queryForm =
    form === 'Region'
      ? 'products_profit_by_regions'
      : 'regions_profit_by_products';

  const getData = async (queryForm) => {
    const resultData = await getAnalysisData(queryForm);
    setAnalysisData(resultData);
  };

  useEffect(() => {
    getData(queryForm);
  }, [form]);

  return analysisData;
}

export default Analysis;
