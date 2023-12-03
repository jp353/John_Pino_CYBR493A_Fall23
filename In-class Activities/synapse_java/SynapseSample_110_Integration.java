/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

package org.apache.synapse.samples.n2n;

import org.apache.synapse.SynapseConstants;

/**
 *
 */
public class SynapseSample_110_Integration extends AbstractAutomationTestCase {

    @Override
    protected void setUp() throws Exception {
        System.setProperty(SynapseConstants.SYNAPSE_XML, SAMPLE_CONFIG_ROOT_PATH + "synapse_sample_110.xml");
//        System.setProperty("addurl", SYNAPSE_BASE_URL + "soap/StockQuoteProxy");
//        System.setProperty("symbol", "IBM");
        // todo : setup the JMS
        super.setUp();
    }

    public void testSample() throws Exception {
//        String resultString = getStringResultOfTest(StockQuoteClient.executeTestClient());
//        assertXpathExists("ns:getQuoteResponse", resultString);
//        assertXpathExists("ns:getQuoteResponse/ns:return", resultString);
    }
}
